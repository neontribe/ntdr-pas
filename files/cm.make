; This file was auto-generated by drush make
core = 7.x

api = 2

; Core
projects[drupal][version] = "7.x"

projects[neontabs][download][tag] = "v_5_16_1"
projects[nt_tabs][download][tag] = "v_5_7_1"
projects[ntcm_modules][download][tag] = "v_0_3_0"
projects[ntcm_theme][download][tag] = "v_0_1_5"

projects[advagg][subdir] = "contrib"
projects[ctools][subdir] = "contrib"
projects[cacheexclude][subdir] = "contrib"
projects[entity][subdir] = "contrib"
projects[field_group][subdir] = "contrib"
projects[globalredirect][subdir] = "contrib"
projects[google_analytics][subdir] = "contrib"
projects[gss][subdir] = "contrib"
projects[imageapi_optimize][subdir] = "contrib"
projects[imagecache_token][subdir] = "contrib"
projects[jquery_update][subdir] = "contrib"
projects[libraries][subdir] = "contrib"
projects[link][subdir] = "contrib"
projects[menu_block][subdir] = "contrib"
projects[menu_expanded][subdir] = "contrib"
projects[metatag][subdir] = "contrib"
projects[references][subdir] = "contrib"
projects[pathauto][subdir] = "contrib"
projects[quicktabs][subdir] = "contrib"
projects[readonlymode][subdir] = "contrib"
projects[redirect][subdir] = "contrib"
projects[seckit][subdir] = "contrib"
projects[site_map][subdir] = "contrib"
projects[superfish][subdir] = "contrib"
projects[token][subdir] = "contrib"
projects[transliteration][subdir] = "contrib"
projects[views][subdir] = "contrib"
projects[webform][subdir] = "contrib"
projects[wysiwyg][subdir] = "contrib"
projects[xmlsitemap][subdir] = "contrib"
projects[xmlsitemap][version] = "2.1"

; Modules
projects[neontabs][download][type] = "git"
projects[neontabs][download][url] = "git@bitbucket.org:neontabs/neontabs.git"
projects[neontabs][type] = "module"
projects[neontabs][subdir] = "custom"

projects[nt_tabs][download][type] = "git"
projects[nt_tabs][download][url] = "git@bitbucket.org:neontabs/nt_tabs.git"
projects[nt_tabs][type] = "module"
projects[nt_tabs][subdir] = "custom"

projects[ntcm_modules][type] = "module"
projects[ntcm_modules][download][type] = "git"
projects[ntcm_modules][download][url] = "git@bitbucket.org:neontabs/ntcm_modules.git"
projects[ntcm_modules][subdir] = "custom"

; Themes
projects[ntcm_theme][type] = "theme"
projects[ntcm_theme][download][type] = "git"
projects[ntcm_theme][download][url] = "git@bitbucket.org:neontabs/ntcm_theme.git"

projects[listingplus][type] = "theme"
projects[listingplus][download][type] = "get"
projects[listingplus][download][url] = "https://staging.neontribe.org/.resources/listingplus.zip"

; Libraries
libraries[tabs-api-client][download][type] = "get"
libraries[tabs-api-client][download][url] = "https://staging.neontribe.org/.resources/tabs-api-client-2.1.zip"
libraries[tabs-api-client][directory_name] = "tabs-api-client"
libraries[tabs-api-client][type] = "library"

libraries[ckeditor][download][type] = "get"
libraries[ckeditor][download][url] = "https://ftp.drupal.org/files/projects/ckeditor-7.x-1.17.zip"
libraries[ckeditor][directory_name] = "ckeditor"
libraries[ckeditor][type] = "library"

libraries[superfish][download][type] = "get"
libraries[superfish][download][url] = "https://github.com/mehrpadin/Superfish-for-Drupal/archive/1.x.zip"
libraries[superfish][directory_name] = "superfish"
libraries[superfish][type] = "library"

