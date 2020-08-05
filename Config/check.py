import re  # import the regex module for using it to find characters


class Check_strength():
    """Check_strength()
        This class contains the function which is responsible for,
        condition of the password i.e secure or not.
    """
    def password_strength(self, password_info):
        """password_strength
                This function checks the strength of the password by checking,
                some of the universal convention used in secure password
        """
        # Check for digits in the password
        print("entered password is : " + password_info)
        digit_error = re.search(r"\d", password_info) is None
        # Check for uppercase characters in the password
        uppercase_error = re.search(r"[A-Z]", password_info) is None
        # Check for lowercase characters in the password
        lowercase_error = re.search(r"[a-z]", password_info) is None
        # Check the condition of the password
        password_condition = not(
            digit_error or
            uppercase_error or
            lowercase_error
        )

        return password_condition  # return the condition of the password


class Check_email():
    def check(self, email):
        # standard email validation condition according to geeksforgeeks
        self.__condition = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if(re.search(self.__condition, email)):
            print("Valid Email")
            return 1
        else:
            print("Invalid Email")
            return 0


class If_only_text():
    def check(self, string):
        regex = re.compile('`[@_!#$%^&*()<>?/\|}{~:]')
        if (re.search("\d", string)) or (regex.search(string)):
            return True
        else:
            return False


class If_only_number():
    def check(self, string):
        regex = re.compile('`[@_!#$%^&*()<>?/\|}{~:]')
        if (regex.search(string)) or re.search("[a-zA-Z]", string):
            return False
        elif (re.search("\d", string)):
            return True
        else:
            return True
