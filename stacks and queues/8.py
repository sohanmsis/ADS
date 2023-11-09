import re

def q5_modified(html_code):
    html_tag_regex = re.compile(r'<([^>]+)>')
    html_tags = html_tag_regex.findall(html_code)

    html_tags_with_attributes = []

    for tag in html_tags:
        attributes = re.findall(r'(\S+)=["\']?((?:.(?!["\']?\s+(?:\S+)=|[>"\']))+.)["\']?', tag)
        html_tags_with_attributes.append((tag, attributes))

    return html_tags_with_attributes

# Test
html_code = '<html><head><title>Page Title</title></head><body><h1 id="header">This is a Heading</h1><p id="para1">This is a paragraph.</p><p id="para2">This is another paragraph.</p></body></html>'

result = q5_modified(html_code)
for tag, attributes in result:
    print(f'Tag: {tag}\nAttributes: {attributes}\n')