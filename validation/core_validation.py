class CoreValidation:
    def isBlank(self, widget, placeholder=""):
        if widget.get() == "" or widget.get() == placeholder:
            return True
        else:
            return False

    def length(string, requiredLength, validity):
        if validity == "greater":
            len(string) < requiredLength?: return True : return False
