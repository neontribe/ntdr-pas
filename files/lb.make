; This file was auto-generated by drush make
core = 7.x
api = 2

; Core
projects[drupal][version] = "7.x"

; Modules
projects[ctools][subdir] = "contrib"
projects[cacheexclude][subdir] = "contrib"
projects[devel][subdir] = "contrib"
projects[entity][subdir] = "contrib"
projects[field_group][subdir] = "contrib"
projects[globalredirect][subdir] = "contrib"
projects[google_analytics][subdir] = "contrib"
projects[httprl][subdir] = "contrib"
projects[imageapi_optimize][subdir] = "contrib"
projects[imagemagick][subdir] = "contrib"
projects[jquery_update][subdir] = "contrib"
projects[libraries][subdir] = "contrib"
projects[link][subdir] = "contrib"
projects[menu_block][subdir] = "contrib"
projects[menu_expanded][subdir] = "contrib"
projects[metatag][subdir] = "contrib"
projects[references][subdir] = "contrib"
projects[pathauto][subdir] = "contrib"
projects[redirect][subdir] = "contrib"
projects[seckit][subdir] = "contrib"
projects[site_map][subdir] = "contrib"
projects[token][subdir] = "contrib"
projects[views][subdir] = "contrib"
projects[webform][subdir] = "contrib"
projects[wysiwyg][subdir] = "contrib"
projects[xmlsitemap][subdir] = "contrib"

; Modules
projects[neontabs][download][type] = "git"
projects[neontabs][download][url] = "git@bitbucket.org:neontabs/neontabs.git"
projects[neontabs][type] = "module"
projects[neontabs][download][tag] = "neontabs_0_14_1"
projects[neontabs][subdir] = "custom"

projects[nt_tabs][download][type] = "git"
projects[nt_tabs][download][url] = "git@bitbucket.org:neontabs/nt_tabs.git"
projects[nt_tabs][type] = "module"
projects[nt_tabs][download][tag] = "nt_tabs_4_12"
projects[nt_tabs][subdir] = "custom"

projects[ntlb_modules][type] = "module"
projects[ntlb_modules][download][type] = "git"
projects[ntlb_modules][download][url] = "git@bitbucket.org:neontabs/ntbr_modules.git"
projects[ntlb_modules][tag] = "2.1.9"
projects[ntlb_modules][subdir] = "custom"

; Themes
projects[ntlb_theme][type] = "theme"
projects[ntlb_theme][download][type] = "git"
projects[ntlb_theme][download][url] = "git@bitbucket.org:neontabs/ntbr_theme.git"
projects[ntlb_theme][download][tag] = "1.3.1"

projects[neontabs_theme][download][type] = "git"
projects[neontabs_theme][download][url] = "git@bitbucket.org:neontabs/neontabs_theme.git"
projects[neontabs_theme][type] = "theme"
projects[neontabs_theme][download][tag] = "3.3.2"

; Libraries
libraries[tabs-api-client][download][type] = "get"
libraries[tabs-api-client][download][url] = "https://jenkins.neontribe.org/drupal/tabs-api-client-2.1.zip"
libraries[tabs-api-client][directory_name] = "tabs-api-client"
libraries[tabs-api-client][type] = "library"

libraries[ckeditor][download][type] = "get"
libraries[ckeditor][download][url] = "https://ftp.drupal.org/files/projects/ckeditor-7.x-1.17.zip"
libraries[ckeditor][directory_name] = "ckeditor"
libraries[ckeditor][type] = "library"

; Profiles
projects[neontabs_profile][download][type] = "git"
projects[neontabs_profile][download][url] = "git@bitbucket.org:neontabs/neontabs_profile.git"
projects[neontabs_profile][download][tag] = "1.0.0"
projects[neontabs_profile][type] = "profile"
