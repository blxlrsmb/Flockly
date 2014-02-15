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

renameTag = (node, name) ->
  unless node.jquery
    node = $(node)
  node2 = $('<'+name+'/>').html node.html()
  node.replaceWith node2
  node2

## Foundation

$(document).foundation()

## Main

if Blockly?
  Blockly.inject $('#blockly')[0],
    path: 'js/blockly/'
    toolbox: $('#toolbox')[0]

$('#search-input').on 'input', ->
  needle = new RegExp($(@).val(), 'i')
  $('#blocks ol').each (_, el) ->
    el.style.display = ''
    renameTag el, 'li'
  $('#blocks li').each (_, el) ->
    unless $('.block-name', el).text().match needle
      x = renameTag(el, 'ol')
      x[0].style.display = 'none'

$('#export-xml').on 'click', (ev) ->
  ev.preventDefault()
  xml = Blockly.Xml.domToText Blockly.Xml.workspaceToDom Blockly.mainWorkspace
  saveData xml, 'meow.xml'

# Blockly Tools..
blocklyTool = {}
blocklyTool.duplicateList = (arr) ->
  ret = []
  arr.forEach((ele) ->
    ret.push([ele, ele])
  )
  return ret

blocklyTool.getFriendField = () ->
  friends = ['Fangrui', 'Qijiang', 'Yuxin', 'Xiaoyu']
  tmplist = blocklyTool.duplicateList(friends)
  return new Blockly.FieldDropdown(tmplist)

window.blocklyTool = blocklyTool
