cs = Flockly.getQueryParams()
id = cs?.id

setName = (name) ->
  $('#name-input').val name

getXML = ->
  Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace

Blockly.inject $('#blockly')[0],
  path: 'js/blockly/'
  toolbox: $('#toolbox')[0]

$.ajaxSetup
  error: ->
    location.replace '/'

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
  if id?
    data.id = id
  $.post uri, data, (id) ->
    history.replaceState null, null, "?id=#{id}"

if id?
  $.getJSON "/get_blockly?id=#{id}", (data) ->
    try
      setName data.name
      dom = Blockly.Xml.textToDom(data.content)
      Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
    catch
