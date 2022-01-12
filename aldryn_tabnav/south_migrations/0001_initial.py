# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TabGroupPlugin'
        db.create_table(u'aldryn_tabnav_tabgroupplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('tab_group_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('layout_template', self.gf('django.db.models.fields.CharField')(default='aldryn_tabnav/tabgroup.html', max_length=200)),
        ))
        db.send_create_signal(u'aldryn_tabnav', ['TabGroupPlugin'])

        # Adding model 'TabPlugin'
        db.create_table(u'aldryn_tabnav_tabplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('tab_title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('tab_extra_icon', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
        ))
        db.send_create_signal(u'aldryn_tabnav', ['TabPlugin'])

        # Adding model 'TabDropDownPlugin'
        db.create_table(u'aldryn_tabnav_tabdropdownplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('tab_title', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal(u'aldryn_tabnav', ['TabDropDownPlugin'])


    def backwards(self, orm):
        # Deleting model 'TabGroupPlugin'
        db.delete_table(u'aldryn_tabnav_tabgroupplugin')

        # Deleting model 'TabPlugin'
        db.delete_table(u'aldryn_tabnav_tabplugin')

        # Deleting model 'TabDropDownPlugin'
        db.delete_table(u'aldryn_tabnav_tabdropdownplugin')


    models = {
        u'aldryn_tabnav.tabdropdownplugin': {
            'Meta': {'object_name': 'TabDropDownPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'tab_title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'aldryn_tabnav.tabgroupplugin': {
            'Meta': {'object_name': 'TabGroupPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'layout_template': ('django.db.models.fields.CharField', [], {'default': "'aldryn_tabnav/tabgroup.html'", 'max_length': '200'}),
            'tab_group_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'aldryn_tabnav.tabplugin': {
            'Meta': {'object_name': 'TabPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'tab_extra_icon': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'tab_title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_tabnav']