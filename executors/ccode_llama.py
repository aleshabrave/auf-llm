from dataclasses import dataclass

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
class CcodeLlamaExecutor(ExecutorInterface):

    _pipe: Pipeline
    _tokenizer: PreTrainedTokenizerFast
    _generation_args: dict

    def __init__(self) -> None:
        model = "codellama/CodeLlama-7b-hf"
        self._tokenizer = AutoTokenizer.from_pretrained(model)
        self._model = AutoTokenizer.from_pretrained(model)
        self._pipe = pipeline(
            "text-generation",
            model=model,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        self._generation_args: dict = {
            "max_new_tokens": 20,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }

    def get_token_cnt(self, text: str) -> None:
        encoded_input = self._tokenizer(
            text, truncation=True, padding=True, return_tensors="pt"
        )

        return len(encoded_input["input_ids"][0])

    def execute(self, system_message: str, user_message: str) -> str:
        messages = [
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ]

        print(messages)
        output = self._pipe(messages, **self._generation_args)
        return output[0]["generated_text"]

    def is_available_msg(
        self, text: str, max_token_cnt: int = 5000
    ) -> tuple[bool, int]:
        token_cnt = self.get_token_cnt(text)

        return token_cnt < max_token_cnt, token_cnt
