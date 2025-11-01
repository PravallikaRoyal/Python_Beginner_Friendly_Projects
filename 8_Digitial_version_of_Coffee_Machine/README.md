The Python Coffee Machine Simulator ☕🤖
Welcome to the command-line coffee machine! This project simulates the core operations of a commercial coffee machine, handling everything from checking resource levels and processing coin payments to serving the final drink.

Commands and Functionality ✨
The simulator recognizes three primary inputs:

1. Order a Drink (e.g., espresso): This is the main function. It checks resources, prompts for coin payment, calculates change, updates the machine's profit, and deducts the used ingredients before serving your coffee.
2. report: This command is for the operator. It prints the current level of water, milk, coffee, and the machine's total profit.
3. off: This is the secret command that stops the simulation and turns off the coffee machine

Code Structure Highlights ☕
The project is built around clear, modular logic:

1. Menu and Resources: All drink specifications (ingredients and cost) are stored in a nested Python dictionary (menu), while the current stock levels are tracked in a separate resources dictionary.
2. Resource Check: The is_resource_sufficient() function ensures the machine has enough ingredients before proceeding to payment.
3. Payment Handling: The process_coins() function takes the user's coin input (quarters, dimes, nickels, pennies) and converts it to a total dollar amount.
4. Transaction Success: The is_transcaction_successful() function manages the finance: it verifies if enough money was received, calculates and prints the change, and updates the global profit variable

This organized approach ensures the code is both functional and easy to maintain.

Contribution 🤝
Got ideas for future development? You could enhance this project by:
Adding input validation to handle typos or non-numeric entries.
Implementing a command to "refill" the resources.
Expanding the menu with new drinks and ingredients.

Feel free to fork the repository and contribute! 🛠️
