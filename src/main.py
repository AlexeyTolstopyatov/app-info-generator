import os
import xml.etree.ElementTree as Node


def main():
    # Initializing
    # Ининциализация корневого элемента
    print("Generating application manifest")
    root: Node.Element = Node.Element("Application")

    # Collecting information
    # Сборка информации
    name: str = input("name=")
    ver: str = input("version=")

    # Writing information
    # Запись информации
    name_tag: Node.Element = Node.SubElement(root, "Name")
    name_tag.text = name
    ver_tag: Node.Element = Node.SubElement(root, "Version")
    ver_tag.text = ver

    # Log it. Save it
    # Сохранение информации
    print("Information Added")

    tree: Node.ElementTree = Node.ElementTree(root)

    tree.write(os.getcwd() + f"\\{name}_manifest.xml")


# Running script like single-file. This file will be not included to somewhere
# Запуск сценария (как единственный файл в проекте). Он никуда не включается
if __name__ == "__main__":
    main()
