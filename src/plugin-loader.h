/*
 * plugin-loader.h — plugin support for telepathy-gabble
 * Copyright © 2009 Collabora Ltd.
 * Copyright © 2009 Nokia Corporation
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */
#ifndef __PLUGIN_LOADER_H__
#define __PLUGIN_LOADER_H__

#include <glib-object.h>
#include <gio/gio.h>

#include <telepathy-glib/base-connection.h>
#include <telepathy-glib/presence-mixin.h>
#include <wocky/wocky.h>

#include "gabble/sidecar.h"
#include "gabble/plugin-connection.h"

typedef struct _GabblePluginLoader GabblePluginLoader;
typedef struct _GabblePluginLoaderClass GabblePluginLoaderClass;
typedef struct _GabblePluginLoaderPrivate GabblePluginLoaderPrivate;

struct _GabblePluginLoaderClass {
    GObjectClass parent_class;
};

struct _GabblePluginLoader {
    GObject parent;

    GabblePluginLoaderPrivate *priv;
};

GType gabble_plugin_loader_get_type (void);

/* TYPE MACROS */
#define GABBLE_TYPE_PLUGIN_LOADER \
  (gabble_plugin_loader_get_type ())
#define GABBLE_PLUGIN_LOADER(obj) \
  (G_TYPE_CHECK_INSTANCE_CAST((obj), GABBLE_TYPE_PLUGIN_LOADER, \
                              GabblePluginLoader))
#define GABBLE_PLUGIN_LOADER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_CAST((klass), GABBLE_TYPE_PLUGIN_LOADER, \
                           GabblePluginLoaderClass))
#define GABBLE_IS_PLUGIN_LOADER(obj) \
  (G_TYPE_CHECK_INSTANCE_TYPE((obj), GABBLE_TYPE_PLUGIN_LOADER))
#define GABBLE_IS_PLUGIN_LOADER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_TYPE((klass), GABBLE_TYPE_PLUGIN_LOADER))
#define GABBLE_PLUGIN_LOADER_GET_CLASS(obj) \
  (G_TYPE_INSTANCE_GET_CLASS ((obj), GABBLE_TYPE_PLUGIN_LOADER, \
                              GabblePluginLoaderClass))

GabblePluginLoader *gabble_plugin_loader_dup (void);

void gabble_plugin_loader_create_sidecar (
    GabblePluginLoader *self,
    const gchar *sidecar_interface,
    GabbleConnection *connection,
    WockySession *session,
    GAsyncReadyCallback callback,
    gpointer user_data);

GabbleSidecar *gabble_plugin_loader_create_sidecar_finish (
    GabblePluginLoader *self,
    GAsyncResult *result,
    GError **error);

TpPresenceStatusSpec *gabble_plugin_loader_append_statuses (
    GabblePluginLoader *self,
    const TpPresenceStatusSpec *base_statuses);

const gchar *gabble_plugin_loader_presence_status_for_privacy_list (
    GabblePluginLoader *loader,
    const gchar *list_name);

GPtrArray * gabble_plugin_loader_create_channel_managers (
    GabblePluginLoader *self,
    GabblePluginConnection *plugin_connection);

#endif /* #ifndef __PLUGIN_LOADER_H__ */
