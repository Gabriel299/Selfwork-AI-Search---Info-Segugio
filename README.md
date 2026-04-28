```

cd info_segugio

poetry install

poetry add chainlit openai tavily-python python-dotenv

Invoke-Expression (poetry env activate) <!-- per Windows -->

chainlit run info_segugio/__init__.py -w

```