class CoreValidation:
    def isBlank(self, widget, placeholder=""):
        if widget == "" or widget == placeholder:
            return True
        else:
            return False

    def length(self, string, requiredLength, validity):
        if validity == "greater":
            return True if len(string) < requiredLength else False
        elif validity == "smaller":
            return True if len(string) > requiredLength else False
        else:
            pass
