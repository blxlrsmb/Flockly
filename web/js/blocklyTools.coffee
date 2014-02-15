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
