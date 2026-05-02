from playwright.sync_api import expect

class BasePage:

    def __init__(self, page):
        self.page = page

    # 🔹 Central locator resolver
    def get_locator(self, role=None, text=None, css=None, test_id=None, label=None, placeholder=None, name=None):
        if role:
            return self.page.get_by_role(role, name=name)
        elif text:
            return self.page.get_by_text(text)
        elif test_id:
            return self.page.get_by_test_id(test_id)
        elif label:
            return self.page.get_by_label(label)
        elif placeholder:
            return self.page.get_by_placeholder(placeholder)
        elif css:
            return self.page.locator(css)
        else:
            raise ValueError("No valid locator provided")

    # 🔹 Click
    def click(self, **locator):
        element = self.get_locator(**locator)
        #expect(element).to_be_visible()
        element.click()

    # 🔹 Fill
    def fill(self, value, **locator):
        element = self.get_locator(**locator)
        element.fill(value)

    # 🔹 Get text
    def get_text(self, **locator):
        element = self.get_locator(**locator)
        return element.text_content()

    # 🔹 Assert visible
    def assert_visible(self, **locator):
        element = self.get_locator(**locator)
        expect(element).to_be_visible()

    # 🔹 Assert URL
    def assert_url_contains(self, text):
        expect(self.page).to_have_url(f"**{text}**")
        
    def accept_cookies(self):
        try:
            self.page.get_by_role("button", name="Accept All").click(timeout=3000)
        except:
         pass  # popup may not always appear
       