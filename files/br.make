; This file was auto-generated by drush make
core = 7.x

api = 2

; Core
projects[drupal][version] = "7.x"

projects[neontabs][download][tag] = v6_1_17
projects[nt_tabs][download][tag] = v5_8_2
projects[ntbr_modules][download][tag] = v2_5_10
projects[ntbr_theme2][download][tag] = v1_0_14


projects[advagg][subdir] = "contrib"
projects[ctools][subdir] = "contrib"
projects[cacheexclude][subdir] = "contrib"
projects[entity][subdir] = "contrib"
projects[field_group][subdir] = "contrib"
projects[globalredirect][subdir] = "contrib"
projects[google_analytics][subdir] = "contrib"
projects[gss][subdir] = "contrib"
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

projects[ntbr_modules][type] = "module"
projects[ntbr_modules][download][type] = "git"
projects[ntbr_modules][download][url] = "git@bitbucket.org:neontabs/ntbr_modules.git"
projects[ntbr_modules][subdir] = "custom"

; Themes
projects[ntbr_theme2][type] = "theme"
projects[ntbr_theme2][download][type] = "git"
projects[ntbr_theme2][download][url] = "git@bitbucket.org:neontabs/ntbr_theme2.git"

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

; Profiles
projects[neontabs_profile][download][type] = "git"
projects[neontabs_profile][download][url] = "git@bitbucket.org:neontabs/neontabs_profile.git"
projects[neontabs_profile][download][tag] = "1.0.0"
projects[neontabs_profile][type] = "profile"
