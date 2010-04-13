find -iname '*.py' | grep -v __init__  | grep -v __path__ | xargs gvim -p
