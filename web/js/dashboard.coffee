## Functions

renameTag = (node, name) ->
  unless node.jquery
    node = $(node)
  node2 = $('<'+name+'/>').html node.html()
  node.replaceWith node2
  node2

## Main

$.ajaxSetup error: -> location.replace '/'

Flockly.getProfile (data, status, xhr) ->
  $('.profile-picture').attr 'src', data.picture.data.url
  $('.profile-name').text data.name

$('#search-input').on 'input', ->
  needle = new RegExp($(@).val(), 'i')
  $('#blocks ol').each (_, el) ->
    el.style.display = ''
    renameTag el, 'li'
  $('#blocks li').each (_, el) ->
    unless $('.block-name', el).text().match needle
      x = renameTag(el, 'ol')
      x[0].style.display = 'none'

$file = $('#xml-file')
$file.on 'change', ->
  if @.files.length > 0
    r = new FileReader
    r.onload = (e) ->
      $.post '/upload_blockly',
        content: e.target.result
        name: 'New Block'
        success: ->
          location.reload()
      $file[0].files.length = 0
    r.readAsText @.files[0]
$('#import-xml').on 'click', ->
  $file.trigger 'click'

blockItemTpt = Handlebars.compile $('#block-item-tpt').html()

$.getJSON '/get_blockly_list', (data) ->
  data.forEach (item) ->
    $('#blocks').append $('<li/>').html blockItemTpt item
