from typing import List

def is_tag_balanced(html: str) -> bool:
    stack: List[str] = []

    tag_open_pos = html.find('<')
    tag_close_pos = html.find('>')

    while tag_open_pos != -1 and tag_close_pos != -1:
        tag_open = html[tag_open_pos + 1:tag_close_pos]
        if not tag_open.startswith('/'):
            stack.append(tag_open)
        else:
            if not stack:
                return False
            if stack[-1] != tag_open[1:]:
                return False
            stack.pop()

        html = html[tag_close_pos + 1:]
        tag_open_pos = html.find('<')
        tag_close_pos = html.find('>')

    return not stack

html = '<html><head><title>Test</title></head><body><h1>Welcome to my test website</h1><p>This is a test paragraph</p></body></html>'
print(is_tag_balanced(html))