#!/usr/bin/python
# -*- coding: utf-8 -*-

lang_dicts = {

	'endict' : {
		"reports_base_url": u"Wikipedia:Database reports/", # The base URL for the report, preceding the page title
		"summary": u"Bot: Updating report",
		"yes-label": u"Yes",
		"no-label": u"No",

		"forgotten-articles-page-title": u"Forgotten articles", # The page title where report is published
		"forgotten-articles-desc": u"List of 500 articles that not been edited in the longest time, ignoring redirects and disambiguation pages.",
		"forgotten-articles-title": u"Title",
		"forgotten-articles-last-edited": u"Last edited",
		"forgotten-articles-editcount": u"Number of edits",

		"pagecount-page-title": u"Page count by namespace",
		"pagecount-desc": u"The number of pages in each [[Wikipedia:Namespace|namespace]]",
		"pagecount-namespace": u"Namespace ID",
		"pagecount-total": u"Total pages",
		"pagecount-redirect": u"Pages with redirects",
		"pagecount-non-redirect": u"Pages without redirects",
		"pagecount-namespace-name": u"Namespace",

		"pagerevisions-page-title": u"Pages with the most revisions",
		"pagerevisions-desc": u"Pages with the most revisions (limited to the first 1000 entries)",
		"pagerevisions-namespace": u"Namespace",
		"pagerevisions-title": u"Article",
		"pagerevisions-revisions": u"Revisions",

		"autopatrol-page-title": u"Editors eligible for Autopatrol privilege",
		"autopatrol-desc": u"List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": u"Username",
		"autopatrol-listlink": u" ",
		"autopatrol-articles": u"Article count",

		"tpbs-page-title": u"Talk pages by size",
		"tpbs-desc": u"Talk pages ranked by total size, including all subpages (e.g. archival subpages, individual WP:RFAs, etc.), to provide statistics on very active discussion pages.",
		"tpbs-namespace": u"Namespace",
		"tpbs-size": u"Size (in MB)",
		"tpbs-page": u"Page",

		"ufr-page-title": u"Unused file redirects",
		"ufr-desc": u"List of file redirects with at most one incoming link, limited to top 500 results.",
		"ufr-page": u"Page",
		"ufr-imagelinks": u"Image Links",
		"ufr-links": u"Links",

		"oldestactive-page-title": u"Active editors with the longest-established accounts",
		"oldestactive-desc": u"The 200 earliest-created editor accounts that have been active in the last thirty days.",
		"oldestactive-username": u"Username",
		"oldestactive-creationdate": u"Date created",
		"oldestactive-editcount": u"Approx. edit count",

		"deletedprods-page-title": u"PRODed articles with deletion logs",
		"deletedprods-desc": u"List of [[WP:PROD|PRODed]] articles that have previously been deleted. Limited to 500 articles.",
		"deletedprods-title": u"Article title",
		"deletedprods-deletecount": u"Delete count",
		"deletedprods-firstdeltime": u"First deletion",
		"deletedprods-lastdeltime": u"Last deletion",
		"deletedprods-delcomments": u"Deletion comments",

		"mostusedtemplate-page-title": u"Templates transcluded on the most pages",
		"mostusedtemplate-desc": u"Templates with the most transclusions (limited to the first 3000 entries)",
		"mostusedtemplate-title": u"Template title",
		"mostusedtemplate-count": u"Number of transclusions",

		"unusedtemplate-page-title": u"Unused templates",
		"unusedtemplate-desc": u"Templates with the no transclusions (limited to the first 2000 entries)",
		"unusedtemplate-title": u"Template title",

		"orphantalk-page-title": u"Orphaned talk pages",
		"orphantalk-desc": u"Orphaned talk pages, limited to 1000",
		"orphantalk-itemtitle": u"Page",
		"orphantalk-namespace": u"Namespace",
		"orphantalk-exists": u"Exists?",
		"orphantalk-isredirect": u"Redirect?",
		"orphantalk-count": u"Count",
		"orphantalk-pagesize": u"Size",

		"article_by_size-page-title": u"Articles by size",
		"article_by_size-desc": u"Articles ranked by total size, principal mainspace.",
		"article_by_size-namespace": u"Namespace",
		"article_by_size-title": u"Article",
		"article_by_size-size": u"Taille",

		"most_edited_page_last_month-page-title": u"Most edited articles last month",
		"most_edited_page_last_month-desc": u"Articles ranked by number of edits during last 30 days, limit to the 25 firsts.",
		"most_edited_page_last_month-title": u"Title",
		"most_edited_page_last_month-editcount": u"Revisions",

		"most_watched-page-title": u"Most-watched pages",
		"most_watched-desc": u"Most-watched non-deleted pages (limited to the first 1000 entries)",
		"most_watched-namespace": u"Namespace",
		"most_watched-title": u"Title",
		"most_watched-watchers": u"Count",
		"most_watched-id": u"N%C2%B0",

		"most_used_external_links-page-title": u"Most used external links",
		"most_used_external_links-desc": u"Most used external links in main namespace by domain (limited to the first 1000 entries)",
		"most_used_external_links-count": u"Count",
		"most_used_external_links-id": u"N%C2%B0",
		"most_used_external_links-domain": u"Domain"
	},

	'esdict' : {
		"forgotten-articles-desc": u"List of non-disambiguation, non-redirect oldest 1000 articles. - Spanish",
		"forgotten-articles-title": u"Title - Spanish",
		"forgotten-articles-last-edited": u"Last edited - Spanish",
		"forgotten-articles-editcount": u"Number of edits - Spanish",

		"pagecount-desc": u"The number of pages in each namespace. - Spanish",
		"pagecount-namespace": u"Namespace - Spanish",
		"pagecount-total": u"Total pages - Spanish",
		"pagecount-redirect": u"Pages with redirects - Spanish",
		"pagecount-non-redirect": u"Pages without redirects - Spanish",
	},

	'dedict' : {
		"reports_base_url": u"Benutzer:Kopiersperre/",

		"forgotten-articles-page-title": u"Vergessene Artikel",
		"forgotten-articles-desc": u"Diese Liste enthält die 1000 Artikel, die am längsten nicht mehr bearbeitet wurden.",
		"forgotten-articles-title": u"Artikel",
		"forgotten-articles-last-edited": u"Letzte Bearbeitung",
		"forgotten-articles-editcount": u"Bearbeitungen insgesamt",
	},

	'testdict': {
		"reports_base_url": u"Wikipedia:Database reports/", # The base URL for the report, preceding the page title
		"summary": u"Bot: Updating report",
		"yes-label": u"Yes",
		"no-label": u"No",

		"forgotten-articles-page-title": u"Forgotten articles", # The page title where report is published
		"forgotten-articles-desc": u"List of 500 articles that not been edited in the longest time, ignoring redirects and disambiguation pages.",
		"forgotten-articles-title": u"Title",
		"forgotten-articles-last-edited": u"Last edited",
		"forgotten-articles-editcount": u"Number of edits",

		"pagecount-page-title": u"Page count by namespace",
		"pagecount-desc": u"The number of pages in each [[Wikipedia:Namespace|namespace]]",
		"pagecount-namespace": u"Namespace ID",
		"pagecount-total": u"Total pages",
		"pagecount-redirect": u"Pages with redirects",
		"pagecount-non-redirect": u"Pages without redirects",
		"pagecount-namespace-name": u"Namespace",

		"pagerevisions-page-title": u"Pages with the most revisions",
		"pagerevisions-desc": u"Pages with the most revisions (limited to the first 1000 entries)",
		"pagerevisions-namespace": u"Namespace",
		"pagerevisions-title": u"Article",
		"pagerevisions-revisions": u"Revisions",

		"tpbs-page-title": u"Talk pages by size",
		"tpbs-desc": u"Talk pages ranked by total size, including all subpages (e.g. archival subpages, individual WP:RFAs, etc.), to provide statistics on very active discussion pages.",
		"tpbs-namespace": u"Namespace",
		"tpbs-size": u"Size (in MB)",
		"tpbs-page": u"Page",

		"ufr-page-title": u"Unused file redirects",
		"ufr-desc": u"List of file redirects with at most one incoming link, limited to top 500 results.",
		"ufr-page": u"Page",
		"ufr-imagelinks": u"Image Links",
		"ufr-links": u"Links",

		"autopatrol-page-title": u"Editors eligible for Autopatrol privilege",
		"autopatrol-desc": u"List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": u"Username",
		"autopatrol-listlink": u" ",
		"autopatrol-articles": u"Article count",

		"oldestactive-page-title": u"Active editors with the longest-established accounts",
		"oldestactive-desc": u"The 200 earliest-created editor accounts that have been active in the last thirty days.",
		"oldestactive-username": u"Username",
		"oldestactive-creationdate": u"Date created",
		"oldestactive-editcount": u"Approx. edit count",

		"deletedprods-page-title": u"PRODed articles with deletion logs",
		"deletedprods-desc": u"Articles which are currently proposed for deletion which have previously been deleted..",
		"deletedprods-title": u"Article title",
		"deletedprods-deletecount": u"Delete count",
		"deletedprods-firstdeltime": u"First deletion",
		"deletedprods-lastdeltime": u"Last deletion",
		"deletedprods-delcomments": u"Deletion comments",

		"mostusedtemplate-page-title": u"Templates transcluded on the most pages",
		"mostusedtemplate-desc": u"Templates with the most transclusions (limited to the first 3000 entries)",
		"mostusedtemplate-title": u"Template title",
		"mostusedtemplate-count": u"Number of transclusions",

		"unusedtemplate-page-title": u"Unused templates",
		"unusedtemplate-desc": u"Templates with the no transclusions (limited to the first 5000 entries)",
		"unusedtemplate-title": u"Template title",

		"orphantalk-page-title": u"Orphaned talk pages",
		"orphantalk-desc": u"Orphaned talk pages, limited to 1000",
		"orphantalk-count": u"Count",
		"orphantalk-itemtitle": u"Page",
		"orphantalk-namespace": u"Namespace",
		"orphantalk-exists": u"Exists?",
		"orphantalk-isredirect": u"Redirect?",
		"orphantalk-pagesize": u"Size",

		"article_by_size-page-title": u"Articles by size",
		"article_by_size-desc": u"Articles ranked by total size, principal mainspace.",
		"article_by_size-namespace": u"Namespace",
		"article_by_size-title": u"Article",
		"article_by_size-size": u"Taille",

		"most_edited_page_last_month-page-title": u"Most edited articles last month",
		"most_edited_page_last_month-desc": u"Articles ranked by number of edits during last 30 days, limit to the 25 firsts.",
		"most_edited_page_last_month-title": u"Title",
		"most_edited_page_last_month-editcount": u"Revisions",

		"most_watched-page-title": u"Most-watched pages",
		"most_watched-desc": u"Most-watched non-deleted pages (limited to the first 1000 entries)",
		"most_watched-namespace": u"Namespace",
		"most_watched-title": u"Title",
		"most_watched-watchers": u"Count",
		"most_watched-id": u"N%C2%B0",

		"most_used_external_links-page-title": u"Most used external links",
		"most_used_external_links-desc": u"Most used external links in main namespace by domain (limited to the first 1000 entries)",
		"most_used_external_links-count": u"Count",
		"most_used_external_links-id": u"N%C2%B0",
		"most_used_external_links-domain": u"Domain"
	},

	'frdict' : {
		"reports_base_url": u"Wikipedia:Rapports/", # The base URL for the report, preceding the page title
		"summary": u"Bot: Mise à jour",
		"yes-label": u"Oui",
		"no-label": u"Non",

		"forgotten-articles-page-title": u"Articles oubliés", # The page title where report is published
		"forgotten-articles-desc": u"Liste des 500 articles qui n'ont pas étés édités depuis le plus longtemps, hors redirections. Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"forgotten-articles-title": u"Titre",
		"forgotten-articles-last-edited": u"Dernière édition",
		"forgotten-articles-editcount": u"Nombre d'éditions",

		"pagecount-page-title": u"Nombre de pages par namespace",
		"pagecount-desc": u"Le nombre d'articles par [[Aide:Espace de noms|espace de nom]] (''namespace''). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"pagecount-namespace": u"Namespace ID",
		"pagecount-total": u"Nombre total de pages",
		"pagecount-redirect": u"Pages avec redirections",
		"pagecount-non-redirect": u"Pages sans redirections",
		"pagecount-namespace-name": u"Namespace",

		"pagerevisions-page-title": u"Pages avec le plus de modifications",
		"pagerevisions-desc": u"Pages avec le plus de modifications (limité aux 1000 premiers articles). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"pagerevisions-namespace": u"Namespace",
		"pagerevisions-title": u"Article",
		"pagerevisions-revisions": u"Modifications",

		"autopatrol-page-title": u"Editors eligible for Autopatrol privilege - right not used ?",
		"autopatrol-desc": u"List of editors who are eligible for the autopatrol privilege and don't have it yet. Limited to 500 users with most articles created.",
		"autopatrol-username": u"Username",
		"autopatrol-listlink": u" ",
		"autopatrol-articles": u"Article count",

		"tpbs-page-title": u"Pages de discussion par taille",
		"tpbs-desc": u"Pages de discussion par leur taille totale, tous espaces de nom confondus, y compris les sous-pages (archives, pages individuelles, PàS, ...). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"tpbs-namespace": u"Namespace",
		"tpbs-size": u"Taille (en MB)",
		"tpbs-page": u"Page",

		"ufr-page-title": u"Unused file redirects - not necessary ?",
		"ufr-desc": u"List of file redirects with at most one incoming link, limited to top 500 results.",
		"ufr-page": u"Page",
		"ufr-imagelinks": u"Image Links",
		"ufr-links": u"Links",

		"oldestactive-page-title": u"Éditeurs actifs avec les comptes les plus anciens",
		"oldestactive-desc": u"Les 200 éditeurs actifs (dernière modification dans les 30 derniers jours) par date de création du compte (à partir du 22 décembre 2005. Pour le moment, les comptes antérieurs ne sont pas listés). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"oldestactive-username": u"Nom d'utilisateur",
		"oldestactive-creationdate": u"Date de création",
		"oldestactive-editcount": u"Compteur d'édition approximatif",

		"deletedprods-page-title": u"PRODed articles with deletion logs - not necessary ?",
		"deletedprods-desc": u"List of [[WP:PROD|PRODed]] articles that have previously been deleted. Limited to 500 articles.",
		"deletedprods-title": u"Article title",
		"deletedprods-deletecount": u"Delete count",
		"deletedprods-firstdeltime": u"First deletion",
		"deletedprods-lastdeltime": u"Last deletion",
		"deletedprods-delcomments": u"Deletion comments",

		"mostusedtemplate-page-title": u"Modèles inclus sur le plus grand nombre de pages",
		"mostusedtemplate-desc": u"Modèles inclus sur le plus grand nombre de pages (limité à 3000)",
		"mostusedtemplate-title": u"Nom du modèle",
		"mostusedtemplate-count": u"Nombre d'inclusions",

		"unusedtemplate-page-title": u"Modèles inutilisés",
		"unusedtemplate-desc": u"Modèles avec le moins d'inclusions (limité à 2000).",
		"unusedtemplate-title": u"Nom du modèle",

		"orphantalk-page-title": u"Pages de discussion orphelines",
		"orphantalk-desc": u"Pages de discussion orphelines (limité à 1000). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"orphantalk-itemtitle": u"Page",
		"orphantalk-namespace": u"Namespace",
		"orphantalk-exists": u"Existe",
		"orphantalk-isredirect": u"Redirection",
		"orphantalk-count": u"Compteur",
		"orphantalk-pagesize": u"Taille",


		"article_by_size-page-title": u"Articles par taille",
		"article_by_size-desc": u"Articles les plus longs (espace principal). Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"article_by_size-namespace": u"Namespace",
		"article_by_size-title": u"Article",
		"article_by_size-size": u"Taille",

		"most_edited_page_last_month-page-title": u"Articles les plus édités le mois dernier",
		"most_edited_page_last_month-desc": u"Liste des 25 articles ayant eu le plus de modifications durant les 30 derniers jours. Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"most_edited_page_last_month-title": u"Titre",
		"most_edited_page_last_month-editcount": u"Nombre d'éditions",

		"most_watched-page-title": u"Pages les plus suivies",
		"most_watched-desc": u"Liste des pages non-supprimées les plus suivies (limitée aux 1 000 premières entrées).  Il est possible de trier une colonne en cliquant sur les deux flèches de son libellé.",
		"most_watched-namespace": u"[[Aide:Espace de noms|NS]]",
		"most_watched-title": u"Titre",
		"most_watched-watchers": u"Nombre",
		"most_watched-id": u"N.",

		"most_used_external_links-page-title": u"Liens externes les plus utilisés dans l'espace principal",
		"most_used_external_links-desc": u"Liens externes les plus utilisés dans l'espace principal par domaine (limited to the first 1000 entries)",
		"most_used_external_links-count": u"Nombre",
		"most_used_external_links-id": u"N.",
		"most_used_external_links-domain": u"Domaine"
	}
}

