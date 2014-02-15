## Functions

saveData = do ->
  a = document.createElement 'a'
  a.style = 'display: none;'
  document.body.appendChild a
  (data, filename) ->
    blob = new Blob([data], type: 'text/xml')
    a.href = URL.createObjectURL blob
    a.download = filename
    a.click()
    URL.revokeObjectURL a.href

## Main

if Blockly?
  Blockly.inject $('#blockly')[0],
    path: 'js/blockly/'
    toolbox: $('#toolbox')[0]

$('#search-input').on 'input', ->
  console.log 3

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  saveData 'hello', 'meow.xml'
