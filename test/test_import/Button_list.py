class Buttonlist:
  def __init__(self, vol_up, text_button):
    self.text_button = text_button
    vol_up = Button(root, text=text_button)
    vol_up.pack()
