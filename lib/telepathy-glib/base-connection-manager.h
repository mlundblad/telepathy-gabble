/*
 * base-connection-manager.h - Header for TpBaseConnectionManager
 *
 * Copyright (C) 2007 Collabora Ltd.
 * Copyright (C) 2007 Nokia Corporation
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

#ifndef __TP_BASE_CONNECTION_MANAGER_H__
#define __TP_BASE_CONNECTION_MANAGER_H__

#include <dbus/dbus-glib.h>
#include <glib-object.h>
#include <telepathy-glib/base-connection.h>
#include <telepathy-glib/svc-connection-manager.h>

G_BEGIN_DECLS

/**
 * TP_CM_BUS_NAME_BASE:
 *
 * The prefix for a connection manager's bus name, to which the CM's name
 * (e.g. "gabble") should be appended.
 */
#define TP_CM_BUS_NAME_BASE    "org.freedesktop.Telepathy.ConnectionManager."

/**
 * TP_CM_OBJECT_PATH_BASE:
 *
 * The prefix for a connection manager's object path, to which the CM's name
 * (e.g. "gabble") should be appended.
 */
#define TP_CM_OBJECT_PATH_BASE "/org/freedesktop/Telepathy/ConnectionManager/"

/**
 * TpCMParamSpec:
 * @name: Name as passed over D-Bus
 * @dtype: D-Bus type signature. We currently support 16- and 32-bit integers
 *         (@gtype is INT), 16- and 32-bit unsigned integers (gtype is UINT),
 *         strings (gtype is STRING) and booleans (gtype is BOOLEAN).
 * @gtype: GLib type, derived from @dtype as above
 * @flags: Some combination of TP_CONN_MGR_PARAM_FLAG_foo
 * @def: Default value, as a (const gchar *) for string parameters, or
         using #GINT_TO_POINTER or #GUINT_TO_POINTER for integer parameters
 * @offset: Offset of the parameter in the opaque data structure. The member
 *          at that offset is expected to be a gint, guint, (gchar *) or
 *          gboolean, depending on @gtype. Alternatively, this may be
 *          G_MAXSIZE, which means the parameter is obsolete, and is
 *          accepted but ignored.
 *
 * Structure representing a connection manager parameter, as accepted by
 * RequestConnection.
 */
typedef struct {
    const gchar *name;
    const gchar *dtype;
    const GType gtype;
    guint flags;
    const gpointer def;
    const gsize offset;
} TpCMParamSpec;

/** 
 * TpCMProtocolSpec:
 * @name: The name which should be passed to RequestConnection for this
 *        protocol.
 * @parameters: An array of #TpCMParamSpec representing the valid parameters
 *              for this protocol, terminated by a #TpCMParamSpec whose name
 *              entry is NULL.
 * @params_new: A function which allocates an opaque data structure to store
 *              the parsed parameters for this protocol. The offset fields
 *              in the members of the @parameters array refer to offsets
 *              within this opaque structure.
 * @params_free: A function which deallocates the opaque data structure
 *               provided by #params_new, including deallocating its
 *               data members (currently, only strings) if necessary.
 *
 * Structure representing a connection manager protocol.
 */
typedef struct {
    const gchar *name;
    const TpCMParamSpec *parameters;
    void *(*params_new) (void);
    void (*params_free) (void *);
} TpCMProtocolSpec;

/** 
 * TpBaseConnectionManager:
 *
 * A base class for connection managers.
 */
typedef struct _TpBaseConnectionManager TpBaseConnectionManager;

/** 
 * TpBaseConnectionManagerClass:
 * @parent_class: The parent class
 * @cm_dbus_name: The name of this connection manager, as used to construct
 *  D-Bus object paths and bus names. Must contain only letters, digits
 *  and underscores, and may not start with a digit. Must be filled in by
 *  subclasses in their class_init function.
 * @protocol_params: An array of #TpCMProtocolSpec structures representing
 *  the protocols this connection manager supports, terminated by a structure
 *  whose name member is %NULL.
 * @new_connection: A #TpBaseConnectionManagerNewConnFunc used to construct
 *  new connections. Must be filled in by subclasses in their class_init
 *  function.
 *
 * The class structure for #TpBaseConnectionManager.
 */
typedef struct _TpBaseConnectionManagerClass TpBaseConnectionManagerClass;

/** 
 * TpBaseConnectionManagerNewConnFunc:
 * @self: The connection manager implementation
 * @proto: The protocol name from the D-Bus request
 * @params_present: A set of integers representing the indexes into the
 *                  array of #TpCMParamSpec of those parameters that were
 *                  present in the request
 * @parsed_params: An opaque data structure as returned by the protocol's
 *                 params_new function, populated according to the
 *                 parameter specifications
 * @error: if not %NULL, used to indicate the error if %NULL is returned
 *
 * A function that will return a new connection according to the
 * parsed parameters; used to implement RequestConnection.
 *
 * The connection manager base class will register the bus name for the
 * new connection, and place a reference to it in its table of
 * connections until the connection's shutdown process finishes.
 *
 * Returns: the new connection object, or %NULL on error.
 */
typedef TpBaseConnection *(*TpBaseConnectionManagerNewConnFunc)(
    TpBaseConnectionManager *self, const gchar *proto,
    TpIntSet *params_present, void *parsed_params, GError **error);

struct _TpBaseConnectionManagerClass {
    GObjectClass parent_class;

    const char *cm_dbus_name;
    const TpCMProtocolSpec *protocol_params;
    TpBaseConnectionManagerNewConnFunc new_connection;
};

struct _TpBaseConnectionManager {
    GObject parent;

    gpointer priv;
};

GType tp_base_connection_manager_get_type(void);

/**
 * tp_base_connection_manager_register:
 * @self: The connection manager implementation
 *
 * Register the connection manager with an appropriate object path as
 * determined from its @cm_dbus_name, and register the appropriate well-known
 * bus name.
 *
 * Returns: %TRUE on success, %FALSE (having emitted a warning to stderr)
 *          on failure
 */
gboolean tp_base_connection_manager_register (TpBaseConnectionManager *self);

/* TYPE MACROS */
#define TP_TYPE_BASE_CONNECTION_MANAGER \
  (tp_base_connection_manager_get_type())
#define TP_BASE_CONNECTION_MANAGER(obj) \
  (G_TYPE_CHECK_INSTANCE_CAST((obj), TP_TYPE_BASE_CONNECTION_MANAGER, TpBaseConnectionManager))
#define TP_BASE_CONNECTION_MANAGER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_CAST((klass), TP_TYPE_BASE_CONNECTION_MANAGER, TpBaseConnectionManagerClass))
#define TP_IS_BASE_CONNECTION_MANAGER(obj) \
  (G_TYPE_CHECK_INSTANCE_TYPE((obj), TP_TYPE_BASE_CONNECTION_MANAGER))
#define TP_IS_BASE_CONNECTION_MANAGER_CLASS(klass) \
  (G_TYPE_CHECK_CLASS_TYPE((klass), TP_TYPE_BASE_CONNECTION_MANAGER))
#define TP_BASE_CONNECTION_MANAGER_GET_CLASS(obj) \
  (G_TYPE_INSTANCE_GET_CLASS ((obj), TP_TYPE_BASE_CONNECTION_MANAGER, TpBaseConnectionManagerClass))

G_END_DECLS

#endif /* #ifndef __TP_BASE_CONNECTION_MANAGER_H__*/
