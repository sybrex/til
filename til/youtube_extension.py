"""
Youtube Extension for Python-Markdown
=====================================
Converts: [youtube]https://www.youtube.com/watch?v=abc[youtube]
Empbeded code: <iframe></iframe>
"""

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class YoutubeExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(YoutubePreprocessor(md), 'youtube', 25)


class YoutubePreprocessor(Preprocessor):
    def run(self, lines):
        text = '\n'.join(lines)
        text = re.sub(
            r'\[youtube\](.*)?v=(.*)\[youtube\]',
            r'<iframe width="560" height="315" src="https://www.youtube.com/embed/\2" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            text
        )
        return text.split('\n')
