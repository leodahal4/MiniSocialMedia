class Clear:
    def this_one(self, *kwargs):
        allwidgets = kwargs
        for i in allwidgets:
            self.widget = i
            self.widget.pi = self.widget.place_info()
            self.widget.place_forget()

