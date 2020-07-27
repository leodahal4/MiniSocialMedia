class Validate:
    def isBlank(self, widget):
        if widget.get() == "":
            return True
        else:
            return False
