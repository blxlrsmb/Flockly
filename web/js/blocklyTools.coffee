# Blockly Tools..
blocklyTool = {}

#$.getJSON '/get_friends', (data) ->
  #blocklyTool.friends = []
  #data.forEach (user) ->
    #username = user['name'] + '/' + user['id']
    #blocklyTool.friends.push(username)

blocklyTool.duplicateList = (arr) ->
  ret = []
  arr.forEach((ele) ->
    ret.push([ele, ele])
  )
  return ret

blocklyTool.getFriendField = () ->
  #friends = ['Fangrui', 'Qijiang', 'Yuxin', 'Xiaoyu']
  tmplist = blocklyTool.duplicateList(blocklyTool.friends)
  return new Blockly.FieldDropdown(tmplist)

window.blocklyTool = blocklyTool
