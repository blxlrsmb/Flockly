cs = Flockly.getQueryParams()
id = cs?.id

setName = (name) ->
  $('#name-input').val name

getName = (name) ->
  $('#name-input').val()

getXML = ->
  Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace

Blockly.inject $('#blockly')[0],
  path: 'js/blockly/'
  toolbox: $('#toolbox')[0]

$.ajaxSetup
  error: ->
    location.replace '/'

Flockly.getProfile (data, status, xhr) ->
  $('.profile-picture').attr 'src', data.picture.data.url
  $('.profile-name').text data.name

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  Flockly.saveData getXML(), getName() or 'block.xml'

$('#import-xml').on 'click', (ev) ->
  ev.preventDefault()
  Flockly.saveData getXML(), getName() or 'block.xml'

$('#save-block').on 'click', (ev) ->
  ev.preventDefault()
  uri = '/upload_blockly'
  uri = "#{uri}?id=#{id}" if id
  data =
    content: getXML()
    name: getName()
  if id?
    data.id = id
  $.post uri, data, (id_) ->
    id = id_
    history.replaceState null, null, "?id=#{id}"

if id?
  $.getJSON "/get_blockly?id=#{id}", (data) ->
    try
      setName data.name
      dom = Blockly.Xml.textToDom(data.content)
      Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
    catch
