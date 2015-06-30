import logging

logging.basicConfig()

log = logging.getLogger('root')
log.setLevel(logging.DEBUG)
log.debug('%(module)s, %(info)s', {'module':'log', 'info':'error'})
log.debug('ok')
log.critical('critical ok')

