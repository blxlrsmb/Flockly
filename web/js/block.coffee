Blockly.inject $('#blockly')[0],
  path: 'js/blockly/'
  toolbox: $('#toolbox')[0]

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  xml = Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace
  Flockly.saveData xml, 'meow.xml'

cs = Flockly.getQueryParams()
id = cs?.id
$.getJSON "/get_blockly?id=#{id}", (data) ->
  try
    dom = Blockly.Xml.textToDom(data?.content)
    Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
  catch
