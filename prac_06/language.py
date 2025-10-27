from prac_06 import programming_language

def main():
    ruby = programming_language("Ruby", "Dynamic", True, 1995)
    python = programming_language("Python", "Dynamic", True, 1991)
    visual_basic = programming_language("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
