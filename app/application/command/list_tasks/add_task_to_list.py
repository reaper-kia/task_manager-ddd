from dataclasses import dataclass

@dataclass(frozen=True)
class AddTaskToListCommand:
   id_list: str
   title_task: str
   description_task: str | None
   is_complete_task: bool = False