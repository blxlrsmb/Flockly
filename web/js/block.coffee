cs = Flockly.getQueryParams()
id = cs?.id

getXML = ->
  Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace

Blockly.inject $('#blockly')[0],
  path: 'js/blockly/'
  toolbox: $('#toolbox')[0]

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  Flockly.saveData getXML(), 'meow.xml'

$('#save-block').on 'click', (ev) ->
  ev.preventDefault()
  uri = '/upload_blockly'
  uri = "#{uri}?id=#{id}" if id
  data =
    content: getXML()
    name: $('#name-input').val()
  if id
    data.id = id
  $.post uri, data

$.getJSON "/get_blockly?id=#{id}", (data) ->
  try
    $('#name-input').val data.name
    dom = Blockly.Xml.textToDom(data.content)
    Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
  catch
