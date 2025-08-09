# Impromptu-Prompt-Generator


# Prompt Generator Script

This Python script provides a simple interactive tool to randomly select and display writing or discussion prompts from various categories. It leverages the random module to pick prompts at random.

# Features

Multiple prompt categories:

CN: Common Nouns (e.g., mountain, river, city)

AN: Abstract Nouns (e.g., anxiety, bravery, wisdom)

FP: Famous People (e.g., Albert Einstein, Beyoncé)

CE: Current Events (e.g., US Congress, COP28 Climate Summit)

Q: Inspirational Quotes (e.g., quotes by Maya Angelou, Albert Einstein)

random: Mix of all categories

User inputs a category code and receives 3 unique random prompts from that category.

# How It Works

The script defines lists of prompts for each category.

The promptSelection function uses random.sample() to select 3 unique items from the chosen list and prints them.

Each category has a dedicated function (promptAN, promptCN, etc.) that calls promptSelection with the appropriate list.

The user is prompted to enter a category code.

The input string is checked against a dictionary of functions (prompt_functions) and the corresponding prompt function is executed.

If the input is invalid, the user is informed.

# Usage

Run the script. When prompted, type one of the following:

AN - Abstract Nouns

CN - Common Nouns

FP - Famous People

CE - Current Events

Q - Quotes

random - Mixed prompts from all categories

# Possible Improvements

Add error handling if the list has fewer than 3 items.

Support repeated prompt generation without rerunning the script.

Allow custom number of prompts to be chosen.

Save selected prompts to a file or clipboard.

Add GUI or web interface for easier use.
