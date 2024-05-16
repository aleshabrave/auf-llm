from dataclasses import dataclass, field

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Pipeline,
    PreTrainedTokenizerFast,
    pipeline,
)

from executors.interface import ExecutorInterface


@dataclass
class PhiMiniExecutor(ExecutorInterface):

    _pipe: Pipeline
    _tokenizer: PreTrainedTokenizerFast
    _model: AutoModelForCausalLM
    _generation_args: dict = field(
        default_factory={
            "max_new_tokens": 20,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }
    )

    def __init__(self) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-128k-instruct"
        )
        self._model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-128k-instruct",
            device_map="cuda",
            torch_dtype="auto",
            trust_remote_code=True,
        )
        self._pipe = pipeline(
            "text-generation",
            model=self._model,
            tokenizer=self._tokenizer,
        )

    def get_token_cnt(self, text: str) -> None:
        encoded_input = self._tokenizer(
            text, truncation=True, padding=True, return_tensors="pt"
        )

        return len(encoded_input["input_ids"][0])

    def execute(self, system_message: list[str], user_message: str) -> str:
        messages = [
            {
                "role": "user",
                "content": system_message[0],
            },
            {
                "role": "assistant",
                "content": system_message[1],
            },
            {"role": "user", "content": user_message},
        ]
        print(messages)
        output = self._pipe(messages, **self._generation_args)
        return output[0]["generated_text"]

    def is_available_msg(
        self, text: str, max_token_cnt: int = 5000
    ) -> tuple[bool, int]:
        token_cnt = self.get_token_cnt(text)

        return token_cnt < max_token_cnt, token_cnt
