from dataclasses import dataclass


@dataclass
class Question:
    text: str = "sample text"
    is_true: bool = False
    explanation: str = "sample explanation"


q1 = Question("test", True, "because")
print(q1.text)

q2 = Question()
print(q2.text)
