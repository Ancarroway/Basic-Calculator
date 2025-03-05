{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"1SRAnmBMKwffZl9dJsU7_QiBJbHtNbT-j","timestamp":1738786301525}],"authorship_tag":"ABX9TyMrAPM2w9N4lSDCx4e+dkSh"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["def display_menu():\n","    print(\"***Welcome to the basic calculator program by Ashley***\")\n","    print(\"Program to perform basic operations of Add, Subtract, Multiply, Divide, and Remainder\")\n","    print(\"\\nMenu:\")\n","    print(\"1. Add\")\n","    print(\"2. Subtract\")\n","    print(\"3. Multiply\")\n","    print(\"4. Divide\")\n","    print(\"5. Remainder\")\n","    print(\"6. Exit\")\n","\n","def get_numbers():\n","    while True:\n","        try:\n","            num1 = float(input(\"Enter the first number: \"))\n","            num2 = float(input(\"Enter the second number: \"))\n","            return num1, num2\n","        except ValueError:\n","            print(\"Invalid input. Please enter numeric values.\")\n","\n","def perform_operation(choice, num1, num2):\n","    if choice == 1:\n","        return num1 + num2\n","    elif choice == 2:\n","        return num1 - num2\n","    elif choice == 3:\n","        return num1 * num2\n","    elif choice == 4:\n","        if num2 == 0:\n","            return \"Error: Division by zero is not allowed.\"\n","        return num1 / num2\n","    elif choice == 5:\n","        if num2 == 0:\n","            return \"Error: Division by zero is not allowed.\"\n","        return num1 % num2\n","\n","def main():\n","    while True:\n","        display_menu()\n","        try:\n","            choice = int(input(\"Select an operation (1-6): \"))\n","            if choice == 6:\n","                print(\"Exiting the program. Goodbye!\")\n","                break\n","            elif choice in [1, 2, 3, 4, 5]:\n","                num1, num2 = get_numbers()\n","                result = perform_operation(choice, num1, num2)\n","                print(f\"Result: {result}\")\n","            else:\n","                print(\"Invalid choice. Please enter a number between 1 and 6.\")\n","        except ValueError:\n","            print(\"Invalid input. Please enter a number between 1 and 6.\")\n","\n","if __name__ == \"__main__\":\n","    main()\n"],"metadata":{"id":"TYYAI4Epi3oF","colab":{"base_uri":"https://localhost:8080/"},"outputId":"efc45d89-ffb1-4ab4-93e4-29ea1bbf655b"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["***Welcome to the basic calculator program by Ashley***\n","Program to perform basic operations of Add, Subtract, Multiply, Divide, and Remainder\n","\n","Menu:\n","1. Add\n","2. Subtract\n","3. Multiply\n","4. Divide\n","5. Remainder\n","6. Exit\n"]}]}]}