class CoreValidation:
    def isBlank(self, widget, placeholder=""):
        if widget.get() == "" or widget.get() == placeholder:
            return True
        else:
            return False
