## Functions

exports = {}
window.Flockly = exports
host = 'http://203.91.121.47:8099'

exports.getProfile = (success, fail) ->
  $.ajax
    url: "#{host}/get_profile"
    dataType: 'json'
    cache: false
    success: success
    error: fail
    crossDomain: true
    xhrFields:
      withCredentials: true

exports.saveData = do ->
  a = document.createElement 'a'
  a.style = 'display: none;'
  document.body.appendChild a
  (data, filename) ->
    blob = new Blob([data], type: 'text/xml')
    a.href = URL.createObjectURL blob
    a.download = filename
    a.click()
    URL.revokeObjectURL a.href

## Foundation

$(document).foundation()

## Main

if Blockly?
  Blockly.inject $('#blockly')[0],
    path: 'js/blockly/'
    toolbox: $('#toolbox')[0]

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  xml = Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace
  exports.saveData xml, 'meow.xml'