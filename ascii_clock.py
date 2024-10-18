#Handles ASCII clock display effectively, giving users the option to choose between 12-hour and 24-hour formats, and allowing them to specify a preferred character for rendering the digits and symbols.

# ----------------------------------------------------------------------------------------------------------------------------------------------
#Asking for inputs

myTime = input('Enter the time: ')
myType = input('Choose the clock type (12 or 24): ')
myChar = input('Enter your preferred character: ')


# ----------------------------------------------------------------------------------------------------------------------------------------------
#Makes sure myChar is allowed

# Ensure the hour part is always two digits for 24-hour format input
if len(myTime) < 5:  # If input is like '3:00' instead of '03:00'
    myTime = '0' + myTime  # Add a leading zero to make it '03:00'

allowed_char = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', '@', '$', '&', '*', '=', '']
myChar_list = list(myChar)

while True:
    if myChar in allowed_char:
        break
        
    elif myChar_list == []:
        break

    else:
        myChar = input("Character not permitted! Try again: ")


# ----------------------------------------------------------------------------------------------------------------------------------------------
#When myChar is blank

if myChar == '':
    mydict = {
        'one': [' ','1',' ',
                '1','1',' ',
                ' ','1',' ',
                ' ','1',' ',
                '1','1','1'],
        'two': ['2','2','2',
                ' ',' ','2',
                '2','2','2',
                '2',' ',' ',
                '2','2','2'],
        'three': ['3','3','3',
                  ' ',' ','3',
                  '3','3','3',
                  ' ',' ','3',
                  '3','3','3'],
        'four': ['4',' ','4',
                 '4',' ','4',
                 '4','4','4',
                 ' ',' ','4',
                 ' ',' ','4'],
        'five': ['5','5','5',
                 '5',' ',' ',
                 '5','5','5',
                 ' ',' ','5',
                 '5','5','5'],
        'six': ['6','6','6',
                '6',' ',' ',
                '6','6','6',
                '6',' ','6',
                '6','6','6'],
        'seven': ['7','7','7',
                  ' ',' ','7',
                  ' ',' ','7',
                  ' ',' ','7',
                  ' ',' ','7'],
        'eight': ['8','8','8',
                  '8',' ','8',
                  '8','8','8',
                  '8',' ','8',
                  '8','8','8'],
        'nine': ['9','9','9',
                 '9',' ','9',
                 '9','9','9',
                 ' ',' ','9',
                 '9','9','9'],
        'colon': ['',' ',' ',
                  '',':',' ',
                  '',' ',' ',
                  '',':',' ',
                  '',' ',' '],
        'zero': ['0','0','0',
                 '0',' ','0',
                 '0',' ','0',
                 '0',' ','0',
                 '0','0','0'],
        'A': [' ','A',' ',
              'A',' ','A',
              'A','A','A',
              'A',' ','A',
              'A',' ','A'],
        'M': ['M',' ',' ',' ','M',
              'M','M',' ','M','M',
              'M',' ','M',' ','M',
              'M',' ',' ',' ','M',
              'M',' ',' ',' ','M'],
        'P': ['P','P','P',
              'P',' ','P',
              'P','P','P',
              'P',' ',' ',
              'P',' ',' ']
}
    # Convert input time to a list of characters
    myTime = list(myTime)

    # Handle 12-hour conversion
    if myType == '12':
        hour = int(''.join(myTime[:2]))  # Get the hour part (first two characters)
        if hour > 12:
            hour -= 12  # Convert to 12-hour format
            period = 'PM'
        elif hour == 0:
            hour = 12  # Handle midnight
            period = 'AM'
        elif hour == 12:
            period = 'PM'  # Noon case
        else:
            period = 'AM'

        # Update the hour part in `myTime` without a leading zero for 12-hour format
        hour_str = str(hour)  # Drop leading zero for single-digit hours
        myTime = list(hour_str + ''.join(myTime[2:]))  # Update myTime with the converted hour
    else:
        period = ''  # 24-hour clock, no period


    # Initialize rows for ASCII output
    row1, row2, row3, row4, row5 = [], [], [], [], []
    combined = [row1, row2, row3, row4, row5]
    slicing = [(0,3),(3,6),(6,9),(9,12),(12,15)]  # for standard 3-width characters
    slicing_M = [(0,5),(5,10),(10,15),(15,20),(20,25)]  # for wider characters like M

    # Character mappings for ASCII digits
    iteration = [[0,'zero'],[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four'], [5, 'five'], 
                 [6, 'six'], [7, 'seven'], [8, 'eight'], [9, 'nine']]

    # Replace default '*' with user's preferred character


    # Process each character in the time input
    for i in myTime:
        if i != ':':
            # Identify and convert numbers to ASCII art
            for n in iteration:
                if int(i) == n[0]:
                    for k in range(5):  # Append rows 1 through 5 for the digit
                        combined[k].append(''.join(mydict[n[1]][slicing[k][0]:slicing[k][1]]))
                    for k in range(5):  # Add space after each digit
                        combined[k].append(' ')
                        
                        
        else:
            # Process colon separately
            for k in range(5):
                combined[k].append(''.join(mydict['colon'][slicing[k][0]:slicing[k][1]]))
            for k in range(5):  # Add space after the colon
                combined[k].append('')

    # Determine AM or PM and add ASCII art if 12-hour clock is selected
    if myType == '12':
        # Process each letter of "AM" or "PM"
        period_letters = list(period)
        for letter in period_letters:
            for k in range(5):
                combined[k].append(' ')  # Spacing before each letter
                if letter == 'M':  # Use wider slicing for M
                    combined[k].append(''.join(mydict[letter][slicing_M[k][0]:slicing_M[k][1]]))
                else:
                    combined[k].append(''.join(mydict[letter][slicing[k][0]:slicing[k][1]]))
                    if len(combined[k]) == 10:
                        combined[k].pop(8)
                    elif len(combined[k]) == 12:
                        combined[k].pop(9)
    else:
        for k in range(5):
            if len(combined[k]) == 10:
                combined[k].pop(9)
            else:
                combined[k].pop(8)
    
# ----------------------------------------------------------------------------------------------------------------------------------------------
#When myChar isn't blank

else:
    mydict = {
        'one': [' ','*',' ',
                '*','*',' ',
                ' ','*',' ',
                ' ','*',' ',
                '*','*','*'],
        'two': ['*','*','*',
                ' ',' ','*',
                '*','*','*',
                '*',' ',' ',
                '*','*','*'],
        'three': ['*','*','*',
                  ' ',' ','*',
                  '*','*','*',
                  ' ',' ','*',
                  '*','*','*'],
        'four': ['*',' ','*',
                 '*',' ','*',
                 '*','*','*',
                 ' ',' ','*',
                 ' ',' ','*'],
        'five': ['*','*','*',
                 '*',' ',' ',
                 '*','*','*',
                 ' ',' ','*',
                 '*','*','*'],
        'six': ['*','*','*',
                '*',' ',' ',
                '*','*','*',
                '*',' ','*',
                '*','*','*'],
        'seven': ['*','*','*',
                  ' ',' ','*',
                  ' ',' ','*',
                  ' ',' ','*',
                  ' ',' ','*'],
        'eight': ['*','*','*',
                  '*',' ','*',
                  '*','*','*',
                  '*',' ','*',
                  '*','*','*'],
        'nine': ['*','*','*',
                 '*',' ','*',
                 '*','*','*',
                 ' ',' ','*',
                 '*','*','*'],
        'colon': ['',' ',' ',
                  '',':',' ',
                  '',' ',' ',
                  '',':',' ',
                  '',' ',' '],
        'zero': ['*','*','*',
                 '*',' ','*',
                 '*',' ','*',
                 '*',' ','*',
                 '*','*','*'],
        'A': [' ','A',' ',
              'A',' ','A',
              'A','A','A',
              'A',' ','A',
              'A',' ','A'],
        'M': ['M',' ',' ',' ','M',
              'M','M',' ','M','M',
              'M',' ','M',' ','M',
              'M',' ',' ',' ','M',
              'M',' ',' ',' ','M'],
        'P': ['P','P','P',
              'P',' ','P',
              'P','P','P',
              'P',' ',' ',
              'P',' ',' ']
    }
    
    



    # Convert input time to a list of characters
    myTime = list(myTime)

    # Handle 12-hour conversion
    if myType == '12':
        hour = int(''.join(myTime[:2]))  # Get the hour part (first two characters)
        if hour > 12:
            hour -= 12  # Convert to 12-hour format
            period = 'PM'
        elif hour == 0:
            hour = 12  # Handle midnight
            period = 'AM'
        elif hour == 12:
            period = 'PM'  # Noon case
        else:
            period = 'AM'

        # Update the hour part in `myTime` without a leading zero for 12-hour format
        hour_str = str(hour)  # Drop leading zero for single-digit hours
        myTime = list(hour_str + ''.join(myTime[2:]))  # Update myTime with the converted hour
    else:
        period = ''  # 24-hour clock, no period

    # Initialize rows for ASCII output
    row1, row2, row3, row4, row5 = [], [], [], [], []
    combined = [row1, row2, row3, row4, row5]
    slicing = [(0,3),(3,6),(6,9),(9,12),(12,15)]  # for standard 3-width characters
    slicing_M = [(0,5),(5,10),(10,15),(15,20),(20,25)]  # for wider characters like M

    # Character mappings for ASCII digits
    iteration = [[0,'zero'],[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four'], [5, 'five'], 
                 [6, 'six'], [7, 'seven'], [8, 'eight'], [9, 'nine']]

    # Replace default '*' with user's preferred character
    if myChar != "*":
        for k in mydict:
            mydict[k] = [myChar if char == '*' else char for char in mydict[k]]

    # Process each character in the time input
    for i in myTime:
        if i != ':':
            # Identify and convert numbers to ASCII art
            for n in iteration:
                if int(i) == n[0]:
                    for k in range(5):  # Append rows 1 through 5 for the digit
                        combined[k].append(''.join(mydict[n[1]][slicing[k][0]:slicing[k][1]]))
                    for k in range(5):  # Add space after each digit
                        combined[k].append(' ')
        else:
            # Process colon separately
            for k in range(5):
                combined[k].append(''.join(mydict['colon'][slicing[k][0]:slicing[k][1]]))
            for k in range(5):  # Add space after the colon
                combined[k].append('')

    # Determine AM or PM and add ASCII art if 12-hour clock is selected
    if myType == '12':
        # Process each letter of "AM" or "PM"
        period_letters = list(period)
        for letter in period_letters:
            for k in range(5):
                combined[k].append(' ')  # Spacing before each letter
                if letter == 'M':  # Use wider slicing for M
                    combined[k].append(''.join(mydict[letter][slicing_M[k][0]:slicing_M[k][1]]))
                    
                else:
                    combined[k].append(''.join(mydict[letter][slicing[k][0]:slicing[k][1]]))
                    if len(combined[k]) == 10:
                        combined[k].pop(8)
                    elif len(combined[k]) == 12:
                        combined[k].pop(9)
    else:
        for k in range(5):
            if len(combined[k]) == 10:
                combined[k].pop(9)
            else:
                combined[k].pop(8)
    
# ----------------------------------------------------------------------------------------------------------------------------------------------
# Prints the Final Number

#Dict for the ASCII


# Convert input time to a list of characters

# Print the ASCII representation
print()
for i in combined:
    print(''.join(i))
