pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'adwaita64')
gnome = import('gnome')

gnome.compile_resources('adwaita64',
  'adwaita64.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'adwaita64.in',
  output: 'adwaita64',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

adwaita64_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(adwaita64_sources, install_dir: moduledir)
