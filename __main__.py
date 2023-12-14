from Bot import Bot, ConsoleInterface

if __name__ == "__main__":
    console_ui = ConsoleInterface()
    bot = Bot()

    console_ui.show_message('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot.book.load("auto_save")
    
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']

    while True:
        action = console_ui.get_user_input()

        if action == 'help':
            console_ui.show_commands(commands)
            action = console_ui.get_user_input()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")

        if action == 'exit':
            break
