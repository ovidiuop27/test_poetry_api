Site:
https://poetrydb.org/index.html

notes:
1. when python read the request results, instead of 'And brought’st Thy sweets along with Thee.' we got 'And broughtâ€™st Thy sweets along with Thee.' so I added  "encoding='utf-8'" when the expected file was read

2. there is a failing test that showcases how deepDiff shows differences, like so:
'values_changed': {"root[53]['title']": {'new_value': "Sonnet XXIII: To Aetna's Scorching Sands", 'old_value': "Sonnet XXIII: To Aetna's Lukewarm Sands"}},
'iterable_item_added': {'root[52]': {'title': 'The Haunted Beach'}}
'iterable_item_removed': {'root[54]': {'title': "Who are you people and where's my horse?!"}}
'repetition_change': {'root[51]': {'old_repeat': 2, 'new_repeat': 1, 'old_indexes': [51, 52], 'new_indexes': [51], 'value': {'title': 'Ode to the Muse'}}}}
