<%inherit file="/base.mako" />

<h2>Submit a Miniconf</h2>
<p>Please read the <a href="${ h.url_for("/programme/miniconf_info") }">Miniconf Info</a> page before submitting a proposal.</p>

${ h.form(h.url_for(), multipart=True) }
<%include file="form_mini.mako" args="editing=False" />

  <p class="submit">${ h.submit('submit', 'Submit!') }</p>
${ h.end_form() }

<%def name="title()" >
Submit a Miniconf - ${ parent.title() }
</%def>
