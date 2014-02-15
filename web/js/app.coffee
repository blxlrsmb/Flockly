## Functions

exports = {}
window.Flockly = exports

exports.getQueryParams = ->
  cs = location.search.substr(1)
  return null unless cs?
  _.chain(cs.split '&').map (param) ->
    p = param.split '='
    [p[0], decodeURIComponent(p[1])]
  .object().value()

exports.getProfile = (success, fail) ->
  $.ajax
    url: "/get_profile"
    dataType: 'json'
    success: success
    error: fail
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
