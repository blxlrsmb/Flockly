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
  $('.profile-picture').css 'background-image', "url(#{data.picture.data.url})"
  $('.profile-name').text data.name

$('#logout').on 'click', ->
  window.location.href = '/logout'

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  name = getName()
  if name == ''
    name = 'block.xml'
  else
    name = "#{name}.xml"
  Flockly.saveData getXML(), name

$file = $('#xml-file')
$file.on 'change', ->
  if @.files.length > 0
    r = new FileReader
    r.onload = (e) ->
      dom = Blockly.Xml.textToDom e.target.result
      Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
    r.readAsText @.files[0]
$('#import-xml').on 'click', (ev) ->
  ev.preventDefault()
  $file.trigger 'click'

$('#clone-block').on 'click', (ev) ->
  ev.preventDefault()
  $.getJSON "/get_blockly?id=#{id}", (data) ->
    delete data.id
    $.post '/upload_blockly', data, (id_) ->
      id = id_
      history.replaceState null, null, "?id=#{id}"

$('#delete-block').on 'click', (ev) ->
  ev.preventDefault()
  $.ajax
    type: 'POST'
    url: '/delete_blockly'
    data: {id}
    success: ->
      location.replace '/dashboard'

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
  tabTpt = Handlebars.compile $('#tab-tpt').html()
  tabContentTpt = Handlebars.compile $('#tab-content-tpt').html()
  $.getJSON "/get_blockly?id=#{id}", (data) ->
    try
      setName data.name
      dom = Blockly.Xml.textToDom(data.content)
      if data.logs?
        data.logs.reverse().forEach (log) ->
          i = $('#log-tabs').children().length
          $('#log-tabs').append tabTpt {i}
          $('#log-tabs-content').append tabContentTpt {i, content: log}
        $('#log-tab-0').parent().addClass 'active'
        $('#log-0').addClass 'active'
      Blockly.Xml.domToWorkspace Blockly.mainWorkspace, dom
    catch
