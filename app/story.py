from typing import TypeAlias

StoryBank: TypeAlias = dict[str, tuple[str, str]]

# Possible stories to be read by the user
STORY: StoryBank = {
    "TheMedicineBag": ("The Medicine Bag", "static\\assets\TheMedicineBag.txt"),
    "LambToSlaughter": ("Lamb To Slaughter", "static\\assets\LambToSlaughter.txt"),
    "NiagaraFalls": ("Niagara Falls", "static\\assets\\NiagaraFalls.txt"),
}
