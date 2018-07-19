# Markdown link formatter

## Alfred setting

``` sh
# convert from reference link to inline style
# /bin/zsh
query=$1

./convertReferenceLinkToInlineLink.py $query
```


``` sh
# convert from inline link to reference style
# /bin/zsh
query=$1

./convertInlineLinkToReferenceLink.py $query
```

