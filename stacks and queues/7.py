class Browser:
    def __init__(self):
        self.stack_forward = []
        self.stack_backward = []
        self.current_url = ''

    def navigate(self, url):
        if url == self.current_url:
            return

        self.stack_backward.append(self.current_url)
        self.current_url = url
        self.stack_forward = []

    def back(self):
        if not self.stack_backward:
            return

        self.stack_forward.append(self.current_url)
        self.current_url = self.stack_backward.pop()

    def forward(self):
        if not self.stack_forward:
            return

        self.stack_backward.append(self.current_url)
        self.current_url = self.stack_forward.pop()

    def __repr__(self):
        return f"Current URL: {self.current_url}\nForward Stack: {self.stack_forward}\nBackward Stack: {self.stack_backward}"

# Example usage
browser = Browser()
browser.navigate('www.google.com')
print(browser)

browser.navigate('www.amazon.com')
print(browser)

browser.back()
print(browser)

browser.forward()
print(browser)