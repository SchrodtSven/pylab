# Core classes 
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-21


variety = 'Stilton'
template = t'Try some {variety} cheese!'
type(template)
#Template objects provide access to the static and interpolated (in curly braces) parts of a string before they are combined. Iterate over Template instances to access their parts in order:

list(template)
#['Try some ', Interpolation('Stilton', 'variety', None, ''), ' cheese!']

