import pywhatkit

txt="""
WordPress websites have an underlying content management system software which makes this type of website flexible and easy to customize.
On the other hand, HTML sites don't have any underlying software — it's all code which can be great if you're a developer, but difficult to manage if you're not."""

pywhatkit.text_to_handwriting(txt,[255,0,0])

print(" END ")
