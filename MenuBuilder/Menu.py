class Menu:
    """ Menu class for runner"""
    def __init__(self, title, options):
        self.title = title
        self.options = options  # options should be a list of tuples (option_name, function_to_call)

    def display(self):
        """ display menu"""
        print(self.title)
        for index, (option_name, _) in enumerate(self.options, start=1):
            print(f"{index}: {option_name}")
        print("0: Exit")

    def run(self):
        """ Run menu"""
        while True:
            self.display()
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    print("Exiting...")
                    break
                elif 1 <= choice <= len(self.options):
                    _, function_to_call = self.options[choice - 1]
                    function_to_call()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Please enter a number.")
            input("Press Enter to continue...")
